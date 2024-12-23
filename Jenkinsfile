pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Am1t-levy/Meme_Generator.git'
            }
        }
        stage('Build') {
            steps {
                echo 'Building the project'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the project'
            }
        }
    }
}
