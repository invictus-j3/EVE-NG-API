#!/usr/bin/python
#
# eve-ng.py
#
# EVE-NG Class

import requests, json, sys, os

class eve_ng(object):
    def __init__(self):
        with open('environment.json') as e:
            self.environ = json.load(e)
            e.close()
        
        ## Setup self variables
        self.session = requests.Session()
        self.headers = {
            'Content-Type' : 'application/json'
        }
        self.auth_headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.base_api_url = 'https://{}/api/'.format(self.environ['server']['ip_address'])

        ## Setup variables for intial authentication
        url = self.base_api_url + 'auth/login'.format(self.environ['server']['ip_address'])
        auth_payload = '{{"username":"{fuser}","password":"{fpass}"}}'.format(fuser=self.environ['credentials']['username'], fpass=self.environ['credentials']['password'])

        # Intial authentication and create cookie
        try:
            s = self.session.post(url, headers=self.auth_headers, verify=False, data=auth_payload)
        except:
            print('ERROR: Authentication API Call Failed\n')
            print('\tURL: {}'.format(url))
            raise SystemExit()
        
        if s.status_code != 200:
            print('Error: Authentication Failure')
            print('Error: HTTP Status Code: {}.'.format(s.status_code))
            print('\tURL: {}'.format(url))
            print('\tAuthentication: {}'.format(auth_payload))
            raise SystemExit(s.status_code)
    
    def api_status(self, response, url, payload='None'):
        if response.status_code == 200:
            return False
        else:
            print('ERROR: API Call Failed\n')
            print('\tURL: {}'.format(url))
            print('\tPayload: {}'.format(payload))
            print('\tResponse: {} ({})'.format(response.text, response.status_code))
            return True
        
    def getlabs(self):
        print('Hold for getlabs')
    
    def start_lab_nodes(self, lab, path=''):
        '''
        Pass lab and path variables as string.\n
        Include the file extention .unl when referencing the lab.\n
        The path variable is optional and will look in the top level of the lab list if not provided.
        '''

        # Get list of lab nodes
        url = self.base_api_url + 'labs/' + path.replace(" ", "%20") + lab.replace(" ", "%20") + '/nodes'
        response = requests.get(url, headers=self.headers, verify=False, cookies=self.session.cookies)        
        r = response.json()
        
        nodes = []
        for d in r['data']:
            nodes.append(d)
        
        # Iterate through the nodes list to start each node
        for n in nodes:
            url = self.base_api_url + 'labs/' + path.replace(" ", "%20") + lab + '/nodes/' + n + '/start'
            response = requests.get(url, headers=self.headers, verify=False, cookies=self.session.cookies)
        return response.status_code

    def stop_lab_nodes(self, lab, path=''):
        '''
        Pass lab and path variables as string.\n
        Include the file extention .unl when referencing the lab.\n
        The path variable is optional and will look in the top level of the lab list if not provided.
        '''

        # Stop all lab nodes
        url = self.base_api_url + 'labs/' + path.replace(" ", "%20") + lab.replace(" ", "%20") + '/nodes/' + 'stop'
        response = requests.get(url, headers=self.headers, verify=False, cookies=self.session.cookies)
        
        return response.status_code