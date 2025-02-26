from Job import Job

class CertbotRenew(Job) :

	def __init__(self, redis_host=None, copy_cache=False) :
		name = "certbot-renew"
		data = ["certbot", "renew", "--deploy-hook", "/opt/bunkerized-nginx/jobs/reload.py"]
		type = "exec"
		super().__init__(name, data, filename=None, redis_host=redis_host, type=type, copy_cache=copy_cache)
