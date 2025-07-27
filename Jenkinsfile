pipeline{
    agent any
    triggers{
        pollSCM('* * * * *')
    }
    stages{
        stage('Checkout'){
            steps{
                echo 'Initializing Git checkout'
                git 'https://github.com/manglamkumar0621/pytest_automation_implementation.git'
            }
        }
        stage('build'){
            steps{
                echo 'Building...'
            }
        }
        stage('Testing'){
            steps{
                echo 'Running tests..'
            }
        }
    }
}