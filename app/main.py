# tool.py

import argparse
import signal
import threading
import time
from app.request import DIRECTORY_BRUTEFORCE
from app.Start_Proxy import start_mitmdump

def main():
    # Argument parser setup
    parser = argparse.ArgumentParser()

    parser.add_argument("-u", "--url", type=str, nargs=1, help="Target URL")
    parser.add_argument("-p", "--PATH", type=str, nargs=1, help="Specify a file or path")
    parser.add_argument("-l", "--log", type=str, nargs=1, help="Specify a log file")
    parser.add_argument("-v", "--verbose", type=int, choices=[1, 2, 3], help="Verbosity")
    parser.add_argument("-CA", "--cert_path", type=str, nargs=1, help="CA certificate path")
    parser.add_argument("-A", "--ALL", action="store_true", help="Try all combinations")
    parser.add_argument("-Pr", "--PROXY", action="store_true", help="Enable proxy support")
    parser.add_argument("-S", "--SAVE", type=str, nargs=1, help="Specify the path to save results.")

    args = parser.parse_args()

    # Global variable for mitmdump process
    proxy_process = None

    def signal_handler(sig, frame):
        """
        Graceful exit on Ctrl+C (SIGINT).
        """
        print("\n[INFO] Terminating proxy and exiting...")
        exit(0)

    # Register the signal handler for Ctrl+C
    signal.signal(signal.SIGINT, signal_handler)

    if args.PROXY:
        print("[INFO] Proxy flag enabled.")
        
        # Start the mitmdump proxy
        def run_proxy():
        
            global proxy_process
            proxy_path = './app/proxy_config.py'
            proxy_process = start_mitmdump(proxy_path)

        proxy_thread = threading.Thread(target=run_proxy, daemon=True)
        proxy_thread.start()

        # Allow time for the proxy to initialize
        time.sleep(1)

    print("[INFO] Starting directory brute-force operation...")
    DIRECTORY_BRUTEFORCE(
        args.PROXY,
        cert_path=args.cert_path,
        file=args.PATH[0],
        url=args.url[0],
        ALL=args.ALL,
        SAVE_PATH=args.SAVE[0]
    )

    print("[INFO] Press ctrl + c to exit ")
    while True:
        time.sleep(1)
