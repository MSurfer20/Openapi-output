### Example 
```perl
use Data::Dumper;
use WWW::OpenAPIClient::StreamsApi;
my $api_instance = WWW::OpenAPIClient::StreamsApi->new(
);

my $subscription_data = [(null)]; # ARRAY[object] | A list of objects that describe the changes that should be applied in each subscription. Each object represents a subscription, and must have a `stream_id` key that identifies the stream, as well as the `property` being modified and its new `value`.  The possible values for each `property` and `value` pairs are:  * `color` (string): the hex value of the user's display color for the stream. * `is_muted` (boolean): whether the stream is   [muted](/help/mute-a-stream).  Prior to Zulip 2.1, this feature was   represented by the more confusingly named `in_home_view` (with the   opposite value, `in_home_view=!is_muted`); for   backwards-compatibility, modern Zulip still accepts that value. * `pin_to_top` (boolean): whether to pin the stream at the top of the stream list. * `desktop_notifications` (boolean): whether to show desktop notifications     for all messages sent to the stream. * `audible_notifications` (boolean): whether to play a sound   notification for all messages sent to the stream. * `push_notifications` (boolean): whether to trigger a mobile push     notification for all messages sent to the stream. * `email_notifications` (boolean): whether to trigger an email     notification for all messages sent to the stream. 

eval { 
    my $result = $api_instance->update_subscription_settings(subscription_data => $subscription_data);
    print Dumper($result);
};
if ($@) {
    warn "Exception when calling StreamsApi->update_subscription_settings: $@\n";
}
```

