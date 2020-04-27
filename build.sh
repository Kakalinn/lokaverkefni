pdflatex -output-directory output verkefni &> out
cd output
bibtex verkefni &> /dev/null
cd ..
pdflatex -output-directory output verkefni &> out
pdflatex -output-directory output verkefni &> out
