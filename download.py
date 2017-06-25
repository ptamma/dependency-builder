#!/usr/bin/env python

import yaml, json, os
from urllib2 import urlopen, URLError, HTTPError

def downloadfile(url):
    # Open the url
    try:
        f = urlopen(url)
        print "downloading " + url

        # Open our local file for writing
        with open(os.path.basename(url), "wb") as local_file:
            local_file.write(f.read())
            
    #handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url


def main():
    # Iterate over image ranges
    with open("/Volumes/yard/sandbox/buildpack/source_repoindex/auto-reconfiguration/index.yml", 'r') as stream:
     try:
         #print(yaml.load(stream))
         fcontent = (yaml.load(stream))
         for release,url in fcontent.iteritems():
             print url
             downloadfile(url)
     except yaml.YAMLError as exc:
        print(exc)
        
if __name__ == '__main__':
    main()