#!/usr/bin/env python
import sys, subprocess
import yaml, json

if __name__ == "__main__":
    
    tests_file = open("entries.yaml", "r")
    tests = yaml.load(tests_file)
    test_name = sys.argv[1]
    success = True
    
    for test_idx,test in enumerate(tests.get(test_name)):
        
        test_in = test.get("in")
        expected_out = test.get("out")
        test_out = subprocess.check_output([str(i) for i in sys.argv[2:] + [test_in]]).strip()
        
        if str(expected_out) == str(test_out):
            result = "\033[92mPASSED\033[0m"
        else:
            result = "\033[91mFAILED!\033[0m Got %s expected %s" % (test_out, expected_out)
            success = False
            
        print "Test %s #%s %s" % (test_name, test_idx+1, result)
        
    sys.exit(0 if success else 1)