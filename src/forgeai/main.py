import argparse
import sys

def main():
    print("Welcome to ForgeAI! Start your local AI agent swarm.")
    # In a full implementation, this would launch Streamlit / FastAPI
    # os.system("streamlit run src/forgeai/ui/app.py")

def cli():
    parser = argparse.ArgumentParser(description="ForgeAI CLI")
    parser.add_argument("command", choices=["serve", "run"], help="Command to execute")
    args = parser.parse_args()

    if args.command == "serve":
        print("Starting ForgeAI web interface on http://localhost:8501...")
        # Add actual Streamlit launch here
    elif args.command == "run":
        print("Running agent swarm from CLI...")

if __name__ == "__main__":
    cli()