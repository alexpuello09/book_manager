import click
import json_manager

@click.group
def cli():
    pass

@cli.command()
@click.option('--title', required = True, help = 'Title of the book')
@click.option('--author', required = True, help = 'Author of the book')
@click.pass_context
def new(ctx, title, author):
    if not title or not author:
        ctx.fail('The title and author are required')
    else:
        data = json_manager.read_json()
        new_id = len(data) + 1
        new_book = {
            "id": new_id,
            "title": title,
            "author": author
            }
        data.append(new_book)
        json_manager.write_json(data)
        print(f"The book {title} created successfully with id {new_id}")

@cli.command()
def users():
    users = json_manager.read_json()
    for user in users:
        print(f"{user['id']} - {user['title']} - {user['author']}")


@cli.command
@click.argument('id', type=int)
def user(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"Book with id {id} not found")
    else:
        print(f"{user['id']} - {user['title']} - {user['author']}")


@cli.command
@click.argument('id', type=int)
def delete(id):
    data = json_manager.read_json()
    user = next((x for x in data if x['id'] == id), None)
    if user is None:
        print(f"Book with id {id} not found")
    else:
        data.remove(user)
        json_manager.write_json(data)
        print(f"Book with id {id} deleted successfully")

@cli.command
@click.argument('id', type=int)
@click.option('--title', help='Title of the book')
@click.option('--author', help='Author of the book')
def update(id, title, author):
    data = json_manager.read_json()
    for user in data:
        if user['id'] == id:
            if title is not None:
                user['title'] = title
            if author is not None:
                user['author'] = author
            break
    json_manager.write_json(data)
    print(f"User with id {id} updated successfully")




if __name__ =='__main__':
    cli()
