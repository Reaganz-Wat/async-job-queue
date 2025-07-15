import asyncio
import time


async def send_email(to, fro, body):
    print(f"Sending email from: {fro} to {to}, and body is: {body}")
    await asyncio.sleep(4)
    print(f"Done doing sending email...")

async def process_subscriptions(amount, subscription_plan="12000", what_subscription="GoTv"):
    print(f"You are subscribing for {what_subscription}, and amount is {amount}, subscription plan is {subscription_plan}")
    await asyncio.sleep(2)
    print(f"Done subscribing...")

# async def main():
#     await asyncio.gather(
#         send_email(to="reaganwatmon6@gmail.com", fro="okellodennis@gmail.com", body="Hello reagan, please send me your account number"),
#         process_subscriptions(60000, subscription_plan="Premium", what_subscription="DSTV")
#     )
#
# asyncio.run(main())