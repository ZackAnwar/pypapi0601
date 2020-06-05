#!/usr/bin/env python3
import http.client

def main():

    ## think of this as setting up the connection
    conn = http.client.HTTPConnection("localhost", 9021)

    ## Send an HTTP request and store the HTTP response
    ##    from our webserver
    conn.request('HEAD', '/')

    ## Returns just the response that has been associated with
    ##    the **conn** object.
    res = conn.getresponse()
    
    ## response status and the reason to the screen.
    print(res.status, res.reason)

if __name__ == "__main__":
    main()

