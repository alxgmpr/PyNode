# PyNode
**Version 0.1**
 
A Python 2.7 script (although easily migratable to 3.6) to generate mass HTTP/S proxies quickly.

Every time the script is run, it generates 50 web proxies in the format of your specification (password auth or IP auth).

## Configuration

You must have a Linode account for this script to work. Once you have signed up with Linode and 
added funds to your account, navigate to https://cloud.linode.com/profile/tokens, and generate a new API key.

Please note that this key is not the same as an API client key, or the traditional API key found on manager.linode.com.
If you use the wrong key type the script will not work and you will run into authentication errors.

Save the API key secret in a textfile called ```apikey.txt```. The other configuration options will be prompted to you
as the program runs.

## Installation and Execution

Make sure you've saved your API key before proceeding. See above.

```
$ pip install -r requirements.txt
$ python main.py
```

## Notes

* Linode accounts have a limit of 20 instances per account. 
* This means one Linode account can create 1000 proxies
* The cost of each instance is $5/month.
* Remember to remove the Linodes from your account after you're done using them (or you will keep being charged)


## Roadmap / Upcoming / Todo

- [ ] Multi-threading support to create multiple VPS at once

## Disclaimer / Legal

I am not responsible for your usage of this script or the proxies created by it. Use at your own risk and do your own research. Proxies should never 
be used for unlawful purposes.