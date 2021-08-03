from stringipy import FluentStringList, FluentString

class TestFluentStringList:

    def test_prefix(self):
        result = FluentStringList(["hello"]) \
            .prefix("\"") \
            .data

        assert result[0] == "\"hello"

    def test_suffix(self):
        result = FluentStringList(["hello", "world"]) \
            .suffix("\"") \
            .data

        assert result[1] == "world\""

    def test_snake_case(self):
        result = FluentStringList(["HelloDarkness"]) \
            .snake_case() \
            .data

        assert result[0] == "hello_darkness"

    def test_join(self):
        result = FluentStringList(["hello", "world"]) \
            .join(", ") \
            .data

        assert result == "hello, world"

class TestFluentString:

    def test_prefix(self):
        result = FluentString("hello") \
            .prefix("\"") \
            .data

        assert result == "\"hello"

    def test_suffix(self):
        result = FluentString("hello") \
            .suffix("\"") \
            .data

        assert result == "hello\""

    def test_snake_case(self):
        result = FluentString("HelloWorld") \
            .snake_case() \
            .data

        assert result == "hello_world"