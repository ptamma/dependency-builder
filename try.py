#!/usr/bin/env python

import os, yaml
dstRoot = "/Volumes/yard/sandbox/buildpack/artifacts"

def main():
    # load range from manifest.yml
    with open("manifest.yml", 'r') as stream:
     try:
         #print(yaml.load(stream))
         range = (yaml.load(stream))
         for dstFolder,srcIndex in range.iteritems():
            dstPath = os.path.join(dstRoot, dstFolder)
            if not os.path.isdir(dstPath):
				os.makedirs(dstPath)
				print srcIndex
     except yaml.YAMLError as exc:
        print(exc)
        
if __name__ == '__main__':
    main()