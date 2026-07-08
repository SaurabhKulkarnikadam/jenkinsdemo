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
                    bat  C:\\Users\\DELL\\AppData\\Local\\Microsoft\\WindowsApps\\python.exe extract.py"
                }
            }
         }
}
