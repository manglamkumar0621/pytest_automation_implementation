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
                echo 'Running tests....'
                echo 'Testing commit webhook'
            }
        }
        stage('Build and Test') {
            steps {
                script {
                    // The test runner will be a separate Docker image
                    sh 'docker build -t my-test-image .'
                    // Execute the tests inside the container
                    sh 'docker run --rm my-test-image'
                }
            }
        }
    }
}