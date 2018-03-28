![speed test example](https://raw.githubusercontent.com/alxgmpr/PyNode/master/proxy-speed-test.png)

# PyNode
**Version 0.2**
 
A Python 2.7 script to generate mass HTTP/S proxies quickly.

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

Let the script run for a little while until you see a success message.

## Best Usage

These HTTP proxies are best purposed for monitoring Shopify sites. However since each batch of 50 proxies uses a single
server, if one proxy gets banned the whole batch will be banned as well. I have had good success using these proxies in 
Dashe and Taskbot. To avoid bans:

* Keep a ratio of 50 proxies per site. Paste those into Dashe settings as proxies to monitor with. I monitor at ~750-1000ms.
* For every task, make another batch of 50 proxies, but *only use one of them as a checkout proxy*. I.e. once a task goes
to checkout, it will use another proxy that *hasnt* been previously used to monitor.
* This can be done for a few tasks (2-3) by using localhost as the checkout proxy.
* Keep a separate batch of monitor proxies on ice in case you encounter bans.
* **Don't** test the proxies while your tasks are running. Test them before you start your tasks. If one of the batch works,
they all work.
* **Don't** use proxies from the same batch in multiple bots. Don't split up the batch.

These aren't rules, but more guidelines based on my experience scraping/botting Shopify over the past ~6 mos. You'll need
to experiment and tweak your own set up

## Notes

* Linode accounts have a limit of 20 instances per account. 
* This means one Linode account can create 1000 proxies
* The cost of each instance is $5/month.
* Remember to remove the Linodes from your account after you're done using them (or you will keep being charged)
* Be sure you install `linode-api` *not* `linode`

## Roadmap / Upcoming / Todo

- [ ] Multi-threading support to create multiple VPS at once

## Disclaimer / Legal

I am not responsible for your usage of this script or the proxies created by it. Use at your own risk and do your own research. Proxies should never 
be used for unlawful purposes.

## F.A.Q.

* Q: **How fast are these proxies?**
* A: That depends. On local networks you can expect ~400-1k ms ping times, depending on how far you are from the east coast.
For best results, run your bot on a east coast VPS. On eastern AWS I average ~120-200ms ping time. (These times are measured from Dashe, other requests will vary)

* Q: **My proxies are banned right from the start**
* A: This happens sometimes. Go into your linode account, delete the non-working server and try again.


* Q: **Are these rotating? Why does this "trick" work?**
* A: No these aren't rotating. While they all share the same IP, Shopify treats them somewhat differently when monitoring.
I don't really know why all this works, but it does for Shopify.


* Q: **Can I sell these to people?**
* A: Can you? Yes. Should you? No. You're effectively selling a single proxy server as 50 proxy servers. Which isn't truthful.
Also Linode probably won't like it—just a guess.


* Q: **Can you help me run this?**
* A: No. If you can't figure this out from this readme, I don't know how to help you. Google. 

## License

MIT License

Copyright (c) 2018 Alex Gompper

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
