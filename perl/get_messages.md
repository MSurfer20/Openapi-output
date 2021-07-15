### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::MessagesApi;
my $api_instance = WWW::OpenAPIClient::MessagesApi->new(
);

my $num_before = 4; # int | The number of messages with IDs less than the anchor to retrieve. 
my $num_after = 8; # int | The number of messages with IDs greater than the anchor to retrieve. 
my $anchor = 42; # OneOfstringinteger | Integer message ID to anchor fetching of new messages. Supports special string values for when the client wants the server to compute the anchor to use:  * `newest`: The most recent message. * `oldest`: The oldest message. * `first_unread`: The oldest unread message matching the   query, if any; otherwise, the most recent message.  The special values of `'newest'` and `'oldest'` are also supported for anchoring the query at the most recent or oldest messages.  **Changes**: String values are new in Zulip 3.0 (feature level 1).  The   `first_unread` functionality was supported in Zulip 2.1.x   and older by not sending anchor and using use_first_unread_anchor.    In Zulip 2.1.x and older, `oldest` can be emulated with   `anchor=0`, and `newest` with `anchor=10000000000000000`   (that specific large value works around a bug in Zulip   2.1.x and older in the `found_newest` return value). 
my $narrow = [(null)]; # ARRAY[object] | The narrow where you want to fetch the messages from. See how to [construct a narrow](/api/construct-narrow). 
my $client_gravatar = true; # boolean | Whether the client supports computing gravatars URLs.  If enabled, `avatar_url` will be included in the response only if there is a Zulip avatar, and will be `null` for users who are using gravatar as their avatar.  This option significantly reduces the compressed size of user data, since gravatar URLs are long, random strings and thus do not compress well. The `client_gravatar` field is set to `true` if clients can compute their own gravatars. 
my $apply_markdown = false; # boolean | If `true`, message content is returned in the rendered HTML format. If `false`, message content is returned in the raw Markdown-format text that user entered. 
my $use_first_unread_anchor = true; # boolean | Legacy way to specify `anchor=\"first_unread\"` in Zulip 2.1.x and older.  Whether to use the (computed by the server) first unread message matching the narrow as the `anchor`.  Mutually exclusive with `anchor`.  **Changes**: Deprecated in Zulip 3.0, replaced by `anchor=\"first_unread\"` instead. 

eval { 
    my $result = $api_instance->get_messages(num_before => $num_before, num_after => $num_after, anchor => $anchor, narrow => $narrow, client_gravatar => $client_gravatar, apply_markdown => $apply_markdown, use_first_unread_anchor => $use_first_unread_anchor);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling MessagesApi->get_messages: $@\n";
}
```

