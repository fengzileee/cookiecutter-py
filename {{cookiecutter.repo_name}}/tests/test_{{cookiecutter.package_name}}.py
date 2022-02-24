{%- if cookiecutter.command_line_interface == "typer" %}
from typer.testing import CliRunner
from {{ cookiecutter.package_name }}.cli import app
{%- elif cookiecutter.command_line_interface == "click" %}
from click.testing import CliRunner
{% endif %}
{%- if cookiecutter.command_line_interface not in ["no", "typer"] %}
from {{ cookiecutter.package_name }}.cli import main
{%- endif %}


def test_main():
{%- if cookiecutter.command_line_interface == "typer" %}
    runner = CliRunner()
    result = runner.invoke(app, ["Joe", "-a", 10])

    assert "Hello, I'm Joe. I'm 10 years old." in result.output
    assert result.exit_code == 0
{%- elif cookiecutter.command_line_interface == "click" %}
    runner = CliRunner()
    result = runner.invoke(main, [])

    assert result.output == "()\n"
    assert result.exit_code == 0
{%- elif cookiecutter.command_line_interface == "argparse" %}
    main([])
{%- elif cookiecutter.command_line_interface == "plain" %}
    assert main([]) == 0
{%- else %}
    pass
{%- endif %}
