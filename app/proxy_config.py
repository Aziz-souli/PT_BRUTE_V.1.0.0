
from datetime import datetime
from mitmproxy import http

# ANSI escape codes for styling
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[36m"
YELLOW = "\033[33m"
GREEN = "\033[32m"
RED = "\033[31m"
BLUE = "\033[34m"

# Print initialization message
print(f"{BOLD}{CYAN}Proxy script with enhanced logging has been loaded!{RESET}")

# Function to format and display request details
def log_request(flow: http.HTTPFlow):
    """
    Logs details about the intercepted HTTP request.
    """
    log_data = (
        f"{BOLD}{GREEN}{YELLOW}[REQUEST DETAILS]{RESET}\n"
        f"{BOLD}{GREEN}Timestamp:{RESET} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"{BOLD}{GREEN}Method:{RESET} {flow.request.method}\n"
        f"{BOLD}{GREEN}URL:{RESET} {flow.request.url}\n"
        f"{BOLD}{GREEN}Headers:{RESET} {dict(flow.request.headers)}\n"
        f"{BOLD}{GREEN}Content Length:{RESET} "
        f"{len(flow.request.content) if flow.request.content else 0} bytes\n"
        f"{'-' * 80}"
    )
    print(f"{CYAN}{log_data}{RESET}")

# Function to format and display response details
def log_response(flow: http.HTTPFlow):
    """
    Logs details about the intercepted HTTP response.
    """
    status_color = GREEN if flow.response.status_code < 400 else RED
    log_data = (
        f"{BOLD}{YELLOW}[RESPONSE DETAILS]{RESET}\n"
        f"{BOLD}{CYAN}Timestamp:{RESET} {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        f"{BOLD}{CYAN}URL:{RESET} {flow.request.url}\n"
        f"{BOLD}{CYAN}Status Code:{RESET} {status_color}{flow.response.status_code}{RESET}\n"
        f"{BOLD}{CYAN}Headers:{RESET} {dict(flow.response.headers)}\n"
        f"{BOLD}{CYAN}Content Length:{RESET} "
        f"{len(flow.response.content) if flow.response.content else 0} bytes\n"
        f"{'-' * 80}"
    )
    print(f"{CYAN}{log_data}{RESET}")

# Intercept requests and log details
def request(flow: http.HTTPFlow) -> None:
    log_request(flow)

# Intercept responses and log details
def response(flow: http.HTTPFlow) -> None:
    log_response(flow)
 