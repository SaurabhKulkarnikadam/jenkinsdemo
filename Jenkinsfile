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
                    bat "python extract.py"
                }
            }
         }
}