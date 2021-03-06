from .main import schema
from graphql.utils import schema_printer
import requests

def generate_schema():
    x = open("schema.graphql", "w")

    x.write(schema_printer.print_schema(schema))
    x.close()


def test():
    t = """
    eyJ0eXAiOiJKV1QiLCJub25jZSI6IjI4bFJfUTFlZm9tVUdGaUhCQ2xJSG5ZRmIxTFNha202am51MnZvVGFXY3MiLCJhbGciOiJSUzI1NiIsIng1dCI6ImpTMVhvMU9XRGpfNTJ2YndHTmd2UU8yVnpNYyIsImtpZCI6ImpTMVhvMU9XRGpfNTJ2YndHTmd2UU8yVnpNYyJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC8zZjQzNjdjYi00YmIxLTQyYjItYjczNi0xNjk5OWMzYzhjM2EvIiwiaWF0IjoxNjUwNDY1NzgyLCJuYmYiOjE2NTA0NjU3ODIsImV4cCI6MTY1MDQ3MTQ1NywiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkUyWmdZQ2hYL1B3dy9uWEN3ZEFsblF2S21sSitSVWVlajhwbnFPM2VVdUhvWUNLMnBSUUEiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IlNJTVAiLCJhcHBpZCI6IjA4ZDcwMTIxLWYwZWYtNDljZC05YWU3LTIwYzcyMzJmYWJhMSIsImFwcGlkYWNyIjoiMCIsImlkdHlwIjoidXNlciIsImlwYWRkciI6IjguMzAuMjM0LjIwOCIsIm5hbWUiOiJNaW5waG9uZSBNeWF0Iiwib2lkIjoiNzE2NDYyYjgtNjNiZC00MmM0LWJmZWQtNWM1MjFiMDI4YjQwIiwicGxhdGYiOiI1IiwicHVpZCI6IjEwMDMyMDAxQ0U3RjEzREQiLCJyaCI6IjAuQVhFQXkyZERQN0ZMc2tLM05oYVpuRHlNT2dNQUFBQUFBQUFBd0FBQUFBQUFBQUNIQUV3LiIsInNjcCI6Im9wZW5pZCBwcm9maWxlIFVzZXIuUmVhZCBlbWFpbCIsInNpZ25pbl9zdGF0ZSI6WyJrbXNpIl0sInN1YiI6ImVQYkZMeF9BdGotWERvc3AyQ2NONDBNMEJndEhrb2otQk9tbkY0OFgxMUEiLCJ0ZW5hbnRfcmVnaW9uX3Njb3BlIjoiQVMiLCJ0aWQiOiIzZjQzNjdjYi00YmIxLTQyYjItYjczNi0xNjk5OWMzYzhjM2EiLCJ1bmlxdWVfbmFtZSI6ImJydWNlQHRlYWNoZXJzdWNlbnRlci5jb20iLCJ1cG4iOiJicnVjZUB0ZWFjaGVyc3VjZW50ZXIuY29tIiwidXRpIjoiMVh0VENJT1NFa2lFZDRVWmoxVXBBQSIsInZlciI6IjEuMCIsIndpZHMiOlsiZjI4YTFmNTAtZjZlNy00NTcxLTgxOGItNmExMmYyYWY2YjZjIiwiNjkwOTEyNDYtMjBlOC00YTU2LWFhNGQtMDY2MDc1YjJhN2E4IiwiNjJlOTAzOTQtNjlmNS00MjM3LTkxOTAtMDEyMTc3MTQ1ZTEwIiwiZmU5MzBiZTctNWU2Mi00N2RiLTkxYWYtOThjM2E0OWEzOGIxIiwiYjc5ZmJmNGQtM2VmOS00Njg5LTgxNDMtNzZiMTk0ZTg1NTA5Il0sInhtc19zdCI6eyJzdWIiOiJ4SlhtNjVYeDRJd2EzMHJBQ0JSUTY1V0p5dk1vZlBPZDV0YlhFOHZjam9jIn0sInhtc190Y2R0IjoxNjQyMDU1MzMxfQ.gv1XVmdzpa8EBSQtigcSlRzuslHWvFRlRSUR2mgNJYG1LSIK2DWGrP9HMoZ7wbRtObu7fUX0gPpxaegkx-2VHZLenBw9iRe4jqJKeXK-i152IooMHXk1URVgZPMRb-zmZzsKoe5cpkZODp6YUgWKmcBEAFzw5qkRgLDR7nYKDllzapii7BaWLSZVaa0B7o_NHiap5Z4kt_YzP0HCYivV5p9mHUpYI1wsLKxSBoi6oewxZilE8xtn5Uye_xGo8qN1m_Ldi48fQW-rWjYJlyZTvqF-y_wN3f-crhDuvB--7GlRs1GAyd4WR5QdI77EGnQF8ni7pIkSIb5GC5F9-UCE7g"""
    x = requests.post("http://127.0.0.1:8000/api/duwin/login", {"token":t})
    print(x.status_code)
    print(x.content)