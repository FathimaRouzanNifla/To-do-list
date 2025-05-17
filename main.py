import asyncio
from cli import ToDoCLI

async def main():
    cli = ToDoCLI()
    await cli.run()

if __name__ == "__main__":
    asyncio.run(main())