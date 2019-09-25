#!/bin/bash

set -e
errors=0

# Run unit tests
python viralverify_bionitio/viralverify_bionitio_test.py || {
    echo "'python python/viralverify_bionitio/viralverify_bionitio_test.py' failed"
    let errors+=1
}

# Check program style
pylint -E viralverify_bionitio/*.py || {
    echo 'pylint -E viralverify_bionitio/*.py failed'
    let errors+=1
}

[ "$errors" -gt 0 ] && {
    echo "There were $errors errors found"
    exit 1
}

echo "Ok : Python specific tests"
