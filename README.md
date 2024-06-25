# Background Remover Web Application

This is a web application built with Flask that allows users to upload images, remove backgrounds using the rembg library, and save both the original and processed images to a MySQL database.

## Features

- Upload an image file.
- Remove the background from the uploaded image using rembg.
- Save both the original and processed images to the `static/uploads` and `static/removed` directories respectively.
- Store image paths in a MySQL database (`bgremover`) using Flask-MySQLdb.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python 3.x
- Flask
- Pillow (PIL)
- rembg
- Flask-MySQLdb

You can install the dependencies using the following command:

```bash
pip install -r requirements.txt
```
```bash
 python app.py
```