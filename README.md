# swampup2017

Repo for the swampupconf

## Shortcomings (this is working notes mainly)

### Preset

Need to work out the preset. Known issue :

* Having plugins installed on the jenkins image -> we can't rely on the assumption that internet will be present during the demo
* Existing admin on jenkins image instead of having to dig in the image for the initial password
* [Actually no, just push the one that exists]Having a pre-existing repo on gitlab
[**easy to be done**]
* Having a pre existing docker repo on artifactory -> meh

### getting admin password on jenkins

```
docker exec -it <hash> cat /var/jenkins_home/secrets/initialAdminPassword
```

### Check out the template repo at swampup template

### Next step :

1. Have the Jenkinsfile in the template recognized
2. Integrate minitwit or some shit as a sample
2. Validate build
3. Validate push
4. Find where to deploy and deploy it
5. Automate setup of the platform as much as possible
