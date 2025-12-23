import asyncio

async def validate_transaction(txn_id: int, amount: float):
    await asyncio.sleep(0.01)
    if amount > 1000:
        raise ValueError(f"Transaction {txn_id} exceeds limit")
    return True


async def confirm_transaction(txn_id: int, amount: float):
    # Fire-and-forget validation (task reference intentionally dropped)
    asyncio.create_task(validate_transaction(txn_id, amount))
    return {"txn_id": txn_id, "status": "confirmed"}


def handle_exception(loop, context):
    # Event loop sees the exception, but the caller does not
    print("EVENT LOOP CAUGHT:", context.get("exception"))


async def main():
    loop = asyncio.get_running_loop()
    loop.set_exception_handler(handle_exception)

    confirmations = []
    for i in range(50):
        result = await confirm_transaction(
            i,
            1500 if i % 5 == 0 else 500
        )
        confirmations.append(result)

    # Allow background tasks to finish
    await asyncio.sleep(0.2)

    print(f"\nUser confirmations: {len(confirmations)}")
    print("Reality: Multiple validations failed silently.")


if __name__ == "__main__":
    asyncio.run(main())
