# swampup2017

Repo for the swampupconf

## Shortcomings (this is working notes mainly)

### Preset

Need to work out the preset. Known issue :

Having plugins installed on the jenkins image -> we can't rely on the assumption that internet will be present during the demo
Existing admin on jenkins image instead of having to dig in the image for the initial password
Having a pre-existing repo on gitlab
[**easy to be done**]Having a pre existing docker repo on artifactory

### getting admin password on jenkins

```
docker exec -it <hash> cat /var/jenkins_home/secrets/initialAdminPassword
```
