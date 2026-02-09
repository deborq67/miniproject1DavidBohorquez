# INF601 - Advanced Programming in Python
# David Bohorquez
# Mini Project 1
 
 
 
 
## Description
 
This project plots the closing stock price over the last 10 trading days of the following companies associated with travel:
* Marriott International Inc (MAR)
* Hilton Hotels Corporation (HLT)
* Royal Caribbean Cruises Ltd (RCL)
* Southwest Airlines Co (LUV)
* Uber Technologies Inc (UBER)

![HLT.png](https://i.ibb.co/39P8XhgH/HLT.png)


## Getting Started
 
### Installing
 
This program was made using Python 3.13.9. Given its simplicity, it should run on any computer that has at least Python 3.13 installed along with the dependencies that follow.

### Dependencies

All dependencies are listed in the requirements.txt document. To install them, execute this command on Python:
 
```
pip install -r requirements.txt
```

### Executing the Program
The program is very simple and can be executed from any directory Python has access to. 
* Download both the `main.py` and `requirements.txt` file. It is highly recommended that you keep them both in the same directory.
* Alternatively, you could download the ZIP and use the extracted directory.
* Run the command listed on the **Dependencies** section if you have not done so already.
* Depending on how your Python installation is set up, execute from the directory either of these commands:
```
python main.py
```
or
```
python3 main.py
```
That's it! You should see 5 graphs similar to the image above in a newly created folder called "charts" representing those travel companies.
## Help
 
**Will this program overwrite any files if a 'charts' folder is already made?**

Mostly not. It will only overwrite files that contain the exact name as the tickers with a PNG format. The `exist_ok=True` parameter was added to ensure no errors were present if the folder already existed.

**Will this work on Python 3.14?**
 
## Authors
  
David Bohorquez
## Version History

* 0.1
    * Initial Release
 
## License
 
This project is licensed under the GNU General Public License - see the LICENSE.md file for details
 
## Acknowledgments
 
These following sources helped immensely in writing this script:
* [strftime Cheat Sheet](https://strftime.org/)
* [The matplotlib.axes and matplotlib.axis sections of the documentation.](https://matplotlib.org/stable/api/)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)