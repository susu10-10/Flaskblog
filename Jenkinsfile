pipeline {
    enviroment {
        registry = '10.5.10.38:5000/flaskr-webapp'
        IMAGE_URL_WITH_TAG = '${registry}:${env.BUILD_NUMBER}'
    }
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh "docker build . -t ${IMAGE_URL_WITH_TAG}"
                }
            }
        }
    }

        stage('Push Docker Image') {
            steps {
                sh ""
                script {
                    // Tag the Docker image with a version or a unique identifier
                    // def dockerTag = "${env.BUILD_NUMBER}"
                    // docker.image('your-image-name').tag("${dockerTag}")

                    // Push the Docker image to a container registry (e.g., Docker Hub)
                    // docker.withRegistry('https://registry.example.com', 'credentials-id') {
                        // docker.image("${dockerTag}").push()
                    }
                }
            }

        stage("Post") {
            steps {
                echo "Successfully, pushed image to the docker registry"
            }
        }

        // Add more stages for other tasks in your Jenkins pipeline
        // For example, stages for testing and deployment.
    }

    // Optionally, you can add post-build actions or notifications.
    // For example, sending an email on failure or success.
    post {
        always {
            // Clean up artifacts or perform other cleanup tasks if needed.
        }
    }
}