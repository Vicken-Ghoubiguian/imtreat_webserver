This project is to develop a webserver which will allow:

* to upload images and treat them by adding many effects,

* to shot photos from the client's webcam and save them,

* to treat them (effects, detection...),

* to record videos from the client's webcam and save them,

* to treat record videos or saved videos (effects, detection...).

Others functionalities could be added.

# prerequisites

### Introduction

To deploy this web application, you must install the following Python packages:

* flask : 

* opencv-contrib-python :

* numpy :

All of that is listed in the `requirements.txt` file.

### If you want develop it...

...you need to install a virtual environment.

Before all, clone the project's repo using this command:

```bash
git clone https://gitlab.imerir.com/eric.ghoubiguian/opencv_webserver
```

Now to install the virtual environment, you must in the project's directory:

```bash
cd opencv_webserver
```

Then you must install the `python3-venv` package as follows:

```bash
sudo apt install python3-venv
```
Once done, you must create your virtual environment in the project repo.

To do this, execute this commande:

```bash
python3 -m venv chosen_name_for_your_virtual_environment //chosen_name_for_your_virtual_environment can be replaced by the name you want
```
Then execute the following command to activate your virtual environment:

```bash
source chosen_name_for_your_virtual_environment/bin/activate
```
Now your prompt must be like that:

```bash
(chosen_name_for_your_virtual_environment) username@machinename:~$
```
If it's the case, congratulations. Finally execute this command to install all required Python packages listed in the requirements.txt file:

```bash
pip3 install -r requirements.txt
```

Now you're ready.

### If you want deploy it...

### Finally

To install all of required Python packages, execute the following command:

```bash
pip3 install -r requirements.txt
```
The previous command will install all the Python packages listed in the `requirements.txt` file.

Congratulations, your're now ready.
