pipeline{
    agent any
    triggers{
        pollSCM('* * * * *')
    }
    stages{
        stages('Checkout'){
            steps{
                echo 'Initializing Git checkout'
                git 'https://github.com/manglamkumar0621/pytest_automation_implementation.git'
            }
        }
        stages('build'){
            steps{
                echo 'Building...'
            }
        }
        stages('Testing'){
            steps{
                echo 'Running tests..'
            }
        }
    }
}