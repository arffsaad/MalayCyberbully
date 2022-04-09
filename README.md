# MalayCyberbully Detection Tool
Ariff Bin Mohd Sa'ad, Final Year Project, UNITEN Putrajaya

This tool is a part of my Final Year Project, and utilizes a TF toolkit from Malaya Toolkit, available here: [Malaya Toolkit](https://malaya.readthedocs.io)

This is a **! WORK IN PROGRESS !**

**Project Description:**

A detection tool capable of detecting a text, preferably from an Instagram post, whether if it contains a cyberbullying attempt. It is specially targetted to detect Bahasa Malaysia posts, since there is a lack of support for this language. 

## About
This tool consists of two parts, the Frontend (using laravel for now) and an API Server (python/flask). The Frontend merely serves as a PoC that helps to show how the tool could work in a web environment. The real tool lives in the python/flask part, where all the actual code for the tool (TF models, logic) resides. 

This is decision is made purely because I am unable to think of a better way to run a python shell in a php environment, so I thought why not seperate these two parts independently, and use APIs? Running the python part every time a Text/String is passed from the frontend is time consuming, as the Malaya Toolkits require to be initialized every time it is imported, not to mention the classification models also require time to initialize. This method allows the python part to live on its own, and work independently while also allowing testing to be made using Postman.

If you think this project can or should be further refined, please do fork & pr. I just want to get my degree and be done with it :')

### Melayu
Peranti ini mempunyai dua bahagian: bahagian Frontend yang menggunakan Laravel, dan juga satu peranti pelayan API menggunakan Flask di dalam Python. Bahagian Frontend bertindak sebagai sebuah Proof-of-concept bagi memberi contoh kepada penggunaan peranti ini di dalam sistem sebenar. Kod-kod sebenar untuk peranti ini terletak di dalam Python module.

Keputusan ini dibuat bagi memudahkan pengaturcaraan kedua-dua bahagian projek, dan juga menjimatkan masa bagi memulakan modul malaya toolkit, kerana setiap kali modul ini dimuatnaikkan, ianya memakan masa yang banyak. Dengan mengaturcara bahagian peranti ramalan secara asing, ianya dapat membuatkan peranti ini sebagai 'standalone' dimana ianya tidak memerlukan masa yang banyak untuk mengaplikasikannya di dalam mana-mana sistem. Ianya juga membolehkan ujian terhadap peranti ini dibuat dengan mudah melalui 'Postman' dalam fasa pembangunan.

Jika anda rasa projek ini boleh atau patut ditambahbaik, sila 'fork' dan lakukan PR untuk repositori ini. Saya hanya ingin menamatkan pengajian saya :)

Dev Update:
adding websocket usage in the project.

## Installation/Usage

For deployment, I'd recommend using ngrok for the websocket, since websocket is client-side.
For local env, stick with localhost and you'll be great.

### For usage with Flask (API server)
set FLASK_APP to point to tf.py, and run flask as usual. The flask app accepts a JSON payload with one compulsory value "captions".

```json
{
    "captions" : "Sentence to be evaluated"
}
```

### For usage with Websocket (Web Server/JS)
Please install [PyWebsocket3](https://github.com/GoogleChromeLabs/pywebsocket3). Move `tf.py` file into the `mod_pywebsocket` folder and then open a Powershell/Terminal in the same folder

- Powershell
```
python .\standalone.py -p 9998 -w ../path/to/tensor_wsh.py folder
# For example, your tensor_wsh.py is in tensor folder, then your path would be ../path/to/tensor
```
- Terminal (Linux)
```
python3 standalone.py -p 9998 -w ../path/to/tensor_wsh.py folder
# For example, your tensor_wsh.py is in tensor folder, then your path would be ../path/to/tensor
```
Now that your websocket server is up and ready, Go to the ui folder, and you can see a html and js file. Open the html file to test it.
Please make sure that your websocket server has finished initializing the tool, which will display `Tool Initialized.` when its done.

You can tweak the js to your needs. Observe the console panel to see it work and debug it.

# REFERENCES

@misc{Malaya, Natural-Language-Toolkit library for bahasa Malaysia, powered by Deep Learning Tensorflow,
  author = {Husein, Zolkepli},
  title = {Malaya},
  year = {2018},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/huseinzol05/malaya}}
}
