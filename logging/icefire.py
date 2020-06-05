import logging
import requests
import argparse
import pprint

BOOK = "https://www.anapioficeandfire.com/api/books"

def main():

    # if you use logging, always describe your logging.basicConfig @ the start
    # default logging level is 'warning', which would skip less severe warnings
    logging.basicConfig(filename='icefire.log', format='%(levelname)s:%(asctime)s %(message)s',\
        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
    
    try:
        # this write
        # INFO: 12/12/2019 11:55:02 AM Program started
        logging.info('Scripting started')
    
        # make a call to the API
        icefire = requests.get(BOOK + "/" + args.bookno)
       
        # force a ZeroDivisionError
        # 10 / 0

        # pretty print the json response
        pprint.pprint(icefire.json())
        
        # write response code to log
        logging.info("API Response Code - " + str(icefire))
        
    # if a program errors, write that error to a log file
    except Exception as err:
        logging.critical(err)
                        
    finally:
        # INFO: 12/12/2019 11:55:02 AM Program ended
        logging.info("Program ended")
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--bookno', help='Enter the book number (integer) to look up.')
    args = parser.parse_args()
    main()

