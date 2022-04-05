# carocr

ref : https://github.com/Mactto/License_Plate_Recognition

# pre-condition

sudo apt update    
sudo apt install tesseract-ocr tesseract-ocr-kor   
sudo apt install libtesseract-dev    
sudo apt install python    
sudo apt install python3-pip  

pip3 install opencv-python        
pip3 install matplotlib    
pip3 install pytesseract      

# upgrade tesseract version 4.1.1 to 5.1.0    
sudo apt-get install software-properties-common    
sudo add-apt-repository ppa:alex-p/tesseract-ocr5     
sudo apt update     
sudo apt install tesseract-ocr     

## how to check tesseract version    
tesseract -v    

# cp traineded kor data    
cp ./tesseract-ocr/tesseract-data/kor.traineddata /usr/share/tesseract-ocr/5/tessdata    

You can find other language date on below github.    
https://github.com/tesseract-ocr/tessdata     


## 라즈베리 파이에서 5.x 버젼이 없다. 직접 다운받아서 빌드 하는걸루....     
https://github.com/tesseract-ocr/tesseract/releases/
## build 방법    
https://tesseract-ocr.github.io/tessdoc/Compiling-–-GitInstallation.html     
$sudo apt-get install automake ca-certificates g++ git libtool libleptonica-dev make pkg-config     
$cd tesseract    
$./autogen.sh    
$./configure     
$make     
$sudo make install     
$sudo ldconfig     

