import os
import sys
import threading
import grpc
from concurrent import futures

# Fix Python path issues
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import withdraw_pb2
    import withdraw_pb2_grpc
except ImportError as e:
    print(f"Critical import error: {e}")
    print("Please generate gRPC files with:")
    print("python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. withdraw.proto")
    sys.exit(1)

# Account data
accounts = {
    "ACCT-1001": 500.00,
    "ACCT-1002": 1000.00,
    "ACCT-1003": 750.00
}
account_lock = threading.Lock()

class WithdrawService(withdraw_pb2_grpc.WithdrawServiceServicer):
    def Withdraw(self, request, context):
        account_id = request.account_id
        amount = request.amount
        
        if amount <= 0:
            return withdraw_pb2.WithdrawResponse(
                success=False,
                new_balance=0,
                message="Amount must be positive"
            )
        
        with account_lock:
            if account_id not in accounts:
                return withdraw_pb2.WithdrawResponse(
                    success=False,
                    new_balance=0,
                    message=f"Account {account_id} not found"
                )
            
            balance = accounts[account_id]
            if amount > balance:
                return withdraw_pb2.WithdrawResponse(
                    success=False,
                    new_balance=balance,
                    message=f"Insufficient funds. Available: ${balance:.2f}"
                )
            
            new_balance = balance - amount
            accounts[account_id] = new_balance
            return withdraw_pb2.WithdrawResponse(
                success=True,
                new_balance=new_balance,
                message=f"Withdrawal successful. New balance: ${new_balance:.2f}"
            )

def serve():
    print("Starting gRPC Server - Initial Balances:")
    for acc, bal in accounts.items():
        print(f"{acc}: ${bal:.2f}")
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    withdraw_pb2_grpc.add_WithdrawServiceServicer_to_server(WithdrawService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Server listening on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()