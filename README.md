# Github-Repository-Transfer
Quick python script for transferring repositories from one account to another.

Let's pretend you're in the job market. You just finished a coding bootcamp and have a ton of project repositories 
that you're really not proud of. They show your ability to learn.. But you are still just beginning your career,
and you would rather not have your potential hire notice all of your naming conventions as they browse your projects.

Here's a **great idea**.

How about you create a brand new account on GitHub for all of your practice projects,
and keep your original for your legitimate ones. That's where this tool comes in!

The general process for transferring one repository from one account to another account is as follows:
1. Log in to your the account with repos you want to transfer
2. Go to a specific repository
3. Click the settings
4. Scroll to the bottom in the "Danger Zone"
5. Click transfer
6. Choose the account you want to transfer to. (Note that this will send an email to the receiving account. There is a handshake that needs
to happen before anything can officially be transfered.)
7. Owner of receiving repositories clicks magic link in email associated with the account.

So! Those are the steps, per repository. It's annoying, especially if you want to transfer 20, 30, or even 50+ repositories.

This tool doesn't do everything for you.. But it at least begins the handshake.

### Steps

**First thing's first**

In addition to having your username's for both accounts, you need a token to use Github's API.
Great way of doing that can be found [here](https://developer.github.com/v3/guides/getting-started/#authentication).
Save this guy off somewhere, and you'll use it in a bit.

**PIP**

Install requests! It is set up in the `pip_requirements.txt` file already, but that is the only package needed.
```
pip install -r requirements.txt
```

**Initialize Transfer Object**

There are a few pieces this program needs to know in order to work correctly. `token`, `username`, and `transfer to`. So let's
set up a TransferRepos instance.
```
>> from transfer import TransferRepos
>> tr = TransferRepos(
    token=<your token goes here>,
    username=<from username>,
    transfer_to=<to username>
)
```
Pretty straightforward overall. It stays easy.

**Transfer Repos**

For everything going from one to another..
```
transfer.main()
```

If you want to keep some repositories in the initial account..
```
transfer.main(keep=["repo_name_1", "repo_name_2", etc])
```
 Just pass them as a list to the keep argument.

 If.. You want to reverse it and say only send what I say..
 ```
 transfer.main(transfer=["repo_name_1", "repo_name_2", etc])
 ```
 Use transfer instead of keep.

 Pretty straightforward overall. I encourage you to look in the `transfer.py` and understand what's going on before running.
 It's a very small file.

 Enjoi, and happy coding :)
