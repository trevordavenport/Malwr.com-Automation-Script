import requests
import os
import subprocess
import optparse
from bs4 import BeautifulSoup


def malwr_submission_check(submission_response):
	'''
	Response (JSON):
	{ "status" : "added", "sha256" : <sha256>, "uuid" : <uuid> }
	'''
	try:


	except Exception as e:
		print e


def malwr_file_submission(API_KEY, FILE_SUBMISSION):
	'''
		Post Template: 'curl -F api_key=<key> -F shared=yes -F file=@/path/to/binary https://malwr.com/api/analysis/add/'
	'''
	try:
		CURL    = "curl -F " + API_KEY + " -F shared=yes " + "file=" + FILE_SUBMISSION + " https://malwr.com/api/analysis/add/"
		RET_VAL = subprocess.Popen(CURL, shell=True, stderr=subprocess.PIPE)
		(output, err) = RET_VAL.communicate()

		print "[*] Malwr.com -- Submitting File " + str(FILE_SUBMISSION) + " for Analysis."

		if (output):
			'''
			Successful Post Request
			'''
			print "[+] Successful File Submission."
			malwr_submission_check(output)
		else:
			#Unsuccessful Submission
			print "[+] Unsuccessful File Submission. Please try again." 
	except Exception as e:
		print e


def main():
    try:
        parser = optparse.OptionParser(usage='Usage: %prog [arguments]', version='%prog 1.0')
        parser.add_option('-k', '--key', help='Argument Takes your Malwr API Key as Input')
        parser.add_option('-f', '--file', help='Argument Takes a single File Name as Input')
        (options, args) = parser.parse_args()
        
        if options.file != None and options.key != None:
            api_key 	    = options.key
            file_submission = options.file
            malwr_file_submission(api_key, file_submission)

        elif options.file == None or options.key == None:
            print "Error: Must provide two arguments. API Key and File to Submit."
            parser.print_help()
    except Exception as e:
        print e

if __name__ == '__main__':
    main()
