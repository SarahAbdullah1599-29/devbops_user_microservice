node{
    
    stage('GitHub Checkout'){
        git branch: 'dev', credentialsId: 'devabdullah0615', url: 'https://github.com/SarahAbdullah1599-29/devbops_user_microservice.git'
    }
    
    stage('DevBops User Test'){
        sh 'python3 Test.py'
    }
    
    stage('Docker Image Build'){
        sh 'docker build -t devabdullah0615/userservice .'
    
    }

    stage('Docker Image Push'){

        withCredentials([string(credentialsId: 'devabdullah0615', variable: 'devabdullah0615')]) {
            sh "docker login -u anishmoktan -p ${devabdullah0615}"
    
            }
        
        sh 'docker push devabdullah0615/userservice'
    
    }

    stage('Run Docker conatiner on Private EC2'){
        def dockerRm = 'docker rm -f devbops_user'
        def dockerRmI = 'docker rmi devabdullah0615/userservice'
        def dockerRun = 'docker run -p 8090:80 -d --name devbops_user devabdullah0615/userservicer'
        sshagent(['docker-server']) {
            sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.75 ${dockerRm}"
            sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.75 ${dockerRmI}"
            sh "ssh -o StrictHostKeyChecking=no ec2-user@172.25.11.75 ${dockerRun}"
           
        }
    }   
}
