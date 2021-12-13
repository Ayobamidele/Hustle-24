# Generated by Django 3.2 on 2021-12-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0027_auto_20211213_0907'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingpaymentcustomer',
            old_name='is_active',
            new_name='active',
        ),
        migrations.AddField(
            model_name='shippingpaymentorder',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='shippingpaymentcustomer',
            name='expiry_year',
            field=models.CharField(choices=[(2044, 2044), (2043, 2043), (2042, 2042), (2041, 2041), (2040, 2040), (2039, 2039), (2038, 2038), (2037, 2037), (2036, 2036), (2035, 2035), (2034, 2034), (2033, 2033), (2032, 2032), (2031, 2031), (2030, 2030), (2029, 2029), (2028, 2028), (2027, 2027), (2026, 2026), (2025, 2025), (2024, 2024), (2023, 2023), (2022, 2022), (2021, 2021), (2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919)], max_length=4),
        ),
        migrations.AlterField(
            model_name='shippingpaymentorder',
            name='expiry_year',
            field=models.CharField(choices=[(2044, 2044), (2043, 2043), (2042, 2042), (2041, 2041), (2040, 2040), (2039, 2039), (2038, 2038), (2037, 2037), (2036, 2036), (2035, 2035), (2034, 2034), (2033, 2033), (2032, 2032), (2031, 2031), (2030, 2030), (2029, 2029), (2028, 2028), (2027, 2027), (2026, 2026), (2025, 2025), (2024, 2024), (2023, 2023), (2022, 2022), (2021, 2021), (2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919)], max_length=4),
        ),
    ]