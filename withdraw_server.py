import threading
import grpc
from concurrent import futures
import withdraw_pb2
import withdraw_pb2_grpc

# Predefined accounts with initial balances
accounts = {
    "ACCT-1001": 500.00,
    "ACCT-1002": 1000.00,
    "ACCT-1003": 750.00
}

# Thread lock to prevent concurrent balance modifications
account_lock = threading.Lock()

class WithdrawService(withdraw_pb2_grpc.WithdrawServiceServicer):
    def Withdraw(self, request, context):
        account_id = request.account_id
        amount = request.amount
        
        with account_lock:  # Ensure thread-safe operations
            # Check if account exists
            if account_id not in accounts:
                return withdraw_pb2.WithdrawResponse(
                    success=False,
                    new_balance=0,
                    message=f"Error: Account {account_id} not found"
                )
            
            current_balance = accounts[account_id]
            
            # Check for insufficient funds
            if amount > current_balance:
                return withdraw_pb2.WithdrawResponse(
                    success=False,
                    new_balance=current_balance,
                    message=f"Error: Insufficient funds. Available: ${current_balance:.2f}"
                )
            
            # Process valid withdrawal
            new_balance = current_balance - amount
            accounts[account_id] = new_balance
            return withdraw_pb2.WithdrawResponse(
                success=True,
                new_balance=new_balance,
                message=f"Withdrawal successful. New balance: ${new_balance:.2f}"
            )

def serve():
    print("Initial Account Balances:")
    for acc_id, balance in accounts.items():
        print(f"{acc_id}: ${balance:.2f}")
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    withdraw_pb2_grpc.add_WithdrawServiceServicer_to_server(WithdrawService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server running on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()