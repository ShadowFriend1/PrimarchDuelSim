pipeline {
    agent any
    stages {
		stage('SonarQube analysis') {
			steps {
    			withSonarQubeEnv(installationName: 'My SonarQube Server') {
					sh 'mvn sonar:sonar'
				}
			}
		}
    }
}
