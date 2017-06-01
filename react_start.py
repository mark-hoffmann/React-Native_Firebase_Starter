import os, sys, io

#Arguments passed in HOME_DIR and PROJECT_NAME

HOME_DIR = sys.argv[1]    #"/Users/MarkHoffmann/Desktop/Project1"
os.chdir(HOME_DIR)
PROJECT_NAME = sys.argv[2]    #"Project1"


print("Initializing Project in path: " + HOME_DIR)
os.system('react-native init ' + PROJECT_NAME)
print("Finished")

os.system('npm install --save-dev eslint-config-react-native')
os.chdir(PROJECT_NAME)
with io.FileIO(".eslintrc.json", "w") as file:
    file.write("{\n\t'extends' : ['react-native'],\n\t'rules' : {\n\t\t'arrow-body-style' : 0\n\t}\n}")

print("Installing node modules")
os.system("npm install --save firebase redux react-redux redux-thunk axios")
print("Finished")

os.system("rm index.ios.js")
os.system("rm index.android.js")

with io.FileIO("index.ios.js", "w") as file:
    file.write("import './app/index';")
with io.FileIO("index.android.js", "w") as file:
    file.write("import './app/index';")

os.system("mkdir app")
os.chdir("app")

os.system("touch index.js")
with io.FileIO("index.js", "w") as file:
    file.write("import React, { Component } from 'react';\nimport {\n\tAppRegistry,\n\tView,\n\tText,\n}\n from 'react-native';\nimport firebase from 'firebase';\nimport ReduxThunk from 'redux-thunk';\nimport { Provider } from 'react-redux';\nimport { createStore, applyMiddleware } from 'redux';\n\n//import settings from './config/settings';\n\nimport reducers from './reducers';\n\nclass App extends Component {\n\tcomponentWillMount() {\n\t\t/*firebase.initializeApp({\n\t\t\tapiKey                 : settings.dev ? settings.DEVELOPMENT.FIREBASE_APIKEY          : settings.PRODUCTION.FIREBASE_APIKEY, \n\t\t\tauthDomain            : settings.dev ? settings.DEVELOPMENT.FIREBASE_AUTHDOMAIN         : settings.PRODUCTION.FIREBASE_AUTHDOMAIN,\n\t\t\tdatabaseURL            : settings.dev ? settings.DEVELOPMENT.FIREBASE_URL                 : settings.PRODUCTION.FIREBASE_URL,\n\t\t\tprojectId            : settings.dev ? settings.DEVELOPMENT.FIREBASE_PRODUCT_ID         : settings.PRODUCTION.FIREBASE_PRODUCT_ID,\n\t\t\tstorageBucket        : settings.dev ? settings.DEVELOPMENT.FIREBASE_STORAGEBUCKET    : settings.PRODUCTION.FIREBASE_STORAGEBUCKET,\n\t\t\tmessagingSenderId    : settings.dev ? settings.DEVELOPMENT.FIREBASE_MESSAGING_ID     : settings.PRODUCTION.FIREBASE_MESSAGING_ID,\n\t\t});*/\n\t}\n\n\trender() {\n\t\t//const store = createStore(reducers, {}, applyMiddleware(ReduxThunk) /*Store Enhancer*/)\n\t\treturn (\n\t\t\t//<Provider store={store}>\n\t\t\t\t<View style={{ flex: 1 }}>\n\t\t\t\t\t<Text>Testing</Text>\n\t\t\t\t\t<Text>Testing</Text>\n\t\t\t\t\t<Text>Testing</Text>\n\t\t\t\t\t<Text>Testing</Text>\n\t\t\t\t\t<Text>Testing</Text>\n\t\t\t\t</View>\n\t\t\t//</Provider>\n\t\t);\n\n\t}\n}\n\nAppRegistry.registerComponent('" + PROJECT_NAME + "', () => App);")

    
os.system("mkdir actions")

os.chdir("actions")
os.system("touch index.js")
os.system("touch types.js")
os.chdir("../")

os.system("mkdir components")
os.system("mkdir config")
os.chdir("config")
os.system("touch images.js")
os.system("touch routes.js")
os.system("touch settings.js")
os.system("touch store.js")
os.system("touch styles.js")
os.chdir("../")

os.system("mkdir fonts")
os.system("mkdir images")

os.system("mkdir helpers")
os.chdir("helpers")
os.system("touch index.js")
os.chdir("../")

os.system("mkdir layouts")
os.system("mkdir lib")
os.system("mkdir reducers")
os.chdir("reducers")
with io.FileIO("index.js", "w") as file:
    file.write("import { combineReducers } from 'redux';\n\nexport default combineReducers({\n\n});")

os.chdir("../")
os.system("mkdir routes")
