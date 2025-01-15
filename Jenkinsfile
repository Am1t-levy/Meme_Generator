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
                script {
                    // Build Docker image
                    bat 'docker build -t meme_generator .'
                    echo 'Building the project completed'
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Deploy Docker container
                    bat 'docker run -d -p 5000:5000 --name meme_generator meme_generator'
                    echo 'Deploying the project'

                    // Wait for the container to be ready
                    bat '''
                    :loop
                    curl http://localhost:5000 || (
                        echo Waiting for app to start...
                        timeout /t 5 > nul
                        goto :loop
                    )
                    '''
                }
            }
        }
    }
    post {
        always {
            stage('Cleanup') {
                steps {
                    script {
                        // Stop and remove the Docker container if it exists
                        bat '''
                        docker ps -q --filter "name=meme_generator" | findstr . && docker stop meme_generator && docker rm meme_generator || echo "No container to clean"
                        '''
                        
                        // Remove the Docker image if needed
                        bat '''
                        docker images -q meme_generator | findstr . && docker rmi meme_generator || echo "No image to remove"
                        '''
                    }
                    echo 'Cleanup completed.'
                }
            }
        }
    }
}



