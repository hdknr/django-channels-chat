from chat.channel.consumers import ChatConsumer
import djclick as click
from logging import getLogger
log = getLogger()


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx):
    pass


@main.command()
@click.argument('group_name')
@click.argument('message')
@click.pass_context
def send(ctx, group_name, message):
    '''Offline Send'''
    ChatConsumer.from_offline(group_name, message)
