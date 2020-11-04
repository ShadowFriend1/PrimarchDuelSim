pipeline {
    agent {
        docker {
            image 'maven:3-alpine' 
            args '-v /root/.m2:/root/.m2 -u root:root'
        }
    }
    stages {
	    stage('Check Versions') {
	        steps {
		        sh '''
		        mvn --version
		        '''
	        }
	    }
		stage('SonarQube analysis') {
			steps {
    			withSonarQubeEnv(installationName: 'My SonarQube Server') {
					sh 'mvn sonar:sonar'
				}
			}
		}
		stage("Quality Gate") {
            steps {
  			    timeout(time: 1, unit: 'HOURS') { 
    			    waitForQualityGate abortPipeline: true
                }
            }
  		}
        stage('Build') {
            steps {
		        sh '''
		        mvn -B -DskipTests clean package
		        '''
            }
        }
        stage('Test') {
            steps {
		        sh '''
		        mvn test
		        '''
            }
            post {
                always {
                    junit 'target/surefire-reports/*.xml'
                }
            }
		}
        stage('Deliver') {
            steps {
		        sh '''
		        ./deliver.sh
		        '''
            }
        }
    }
}
