pipeline{

         agent any

         stages{
            stage('checkout code'){
                steps{
                      checkout scm
                }
            }
             stage('run extract.py'){
                steps{
                    bat  C:\\Users\\DELL\\AppData\\Local\\Python\\pythoncore-3.14-64\\python.exe extract.py"
                }
            }
         }
}
