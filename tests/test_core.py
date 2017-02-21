import pytest
import elixr



class TestAttrDict(object):
    def test_is_instance_of_dict(self):
        attrd = elixr.AttrDict()
        assert isinstance(attrd, dict) == True
    
    def test_can_element_using_dot_notation(self):
        foo = elixr.AttrDict()
        foo['bar'] = 'egg-whl'
        assert 'egg-whl' == foo.bar
    
    def test_access_using_unknown_member_returns_None(self):
        attrd = elixr.AttrDict()
        assert None == attrd.bar
    
    def test_access_using_missing_key_returns_None(self):
        attrd = elixr.AttrDict()
        assert None == attrd['bar']

    def test_has_friendly_string_repr(self):
        attrd = elixr.AttrDict(bar='egg-whl')
        assert repr(attrd).startswith('<AttrDict')
    
    def test_make_not_given_dict_or_sequence_fails(self):
        with pytest.raises(ValueError):
            elixr.AttrDict.make('foo')
    
    def test_can_make_attr_dict_from_dict(self):
        foo = elixr.AttrDict.make(dict(bar='egg-whl'))
        assert isinstance(foo, elixr.AttrDict) \
           and 'egg-whl' == foo.bar
    
    def test_can_make_attr_dict_from_nested_dict(self):
        attrd = elixr.AttrDict.make(dict(
            conf = dict(
                name = 'norf',
                meta = dict(name='simple.conf', path=r'c:\path\to\conf')
            )
        ))
        assert isinstance(attrd, elixr.AttrDict) \
           and isinstance(attrd.conf, elixr.AttrDict) \
           and isinstance(attrd.conf.meta, elixr.AttrDict)
