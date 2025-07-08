import grpc
import withdraw_pb2
import withdraw_pb2_grpc

def run_client():
    channel = grpc.insecure_channel('localhost:50051')
    stub = withdraw_pb2_grpc.WithdrawServiceStub(channel)
    
    while True:
        print("\n--- New Withdrawal Request ---")
        account_id = input("Enter Account ID (e.g. ACCT-1001): ").strip()
        amount_str = input("Enter Withdrawal Amount: ").strip()
        
        # Validate numeric input
        try:
            amount = float(amount_str)
            if amount <= 0:
                print("Error: Amount must be positive")
                continue
        except ValueError:
            print("Error: Invalid amount. Please enter a valid number")
            continue
        
        # Create request
        request = withdraw_pb2.WithdrawRequest(
            account_id=account_id,
            amount=amount
        )
        
        # Call gRPC server
        try:
            response = stub.Withdraw(request)
            if response.success:
                print(f"✅ SUCCESS: {response.message}")
            else:
                print(f"❌ FAILED: {response.message}")
        except grpc.RpcError as e:
            print(f"Connection error: {e.details()}")
        
        # Continue?
        if input("\nAnother transaction? (y/n): ").lower() != 'y':
            break

if __name__ == '__main__':
    run_client()