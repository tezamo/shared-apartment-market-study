{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e824d841-b770-417f-8238-96818a442ec2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .

       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .

       removed for privacy concerns
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .
       .

    "        if city_district and \"Berlin\" in city_district:\n",
    "            district = city_district.replace(\"Berlin\", \"\").strip()\n",
    "\n",
    "    # Remove extra spaces between dates in availability\n",
    "    availability_text = availability.text.strip().replace(' ', '') if availability else None\n",
    "\n",
    "    data = {\n",
    "        'Title': title.text.strip() if title else None,\n",
    "        'WG Type': wg_type,\n",
    "        'City/District': district,\n",
    "        'Street': street,\n",
    "        'Price': f\"{price.text.strip().replace('€', '').replace(' ', '')} €\" if price else None,\n",
    "        'Availability': availability_text,\n",
    "        'Size': f\"{size.text.strip().replace('m²', '').replace(' ', '')} m²\" if size else None,\n",
    "        'Owner': owner.text.strip() if owner else None,\n",
    "        'Online Duration': online_duration.text.strip() if online_duration else None\n",
    "    }\n",
    "\n",
    "    return data\n",
    "\n",
    "def scrape_wg_data(base_url, num_listings):\n",
    "    listings_data = []\n",
    "    page = 0\n",
    "\n",
    "    while len(listings_data) < num_listings:\n",
    "        url = f\"{base_url}?page={page}\"\n",
    "        soup = get_wg_listings(url)\n",
    "        listings = soup.find_all('div', class_='offer_list_item')\n",
    "        \n",
    "        if not listings:\n",
    "            break\n",
    "\n",
    "        for listing in listings:\n",
    "            data = parse_listing(listing)\n",
    "            listings_data.append(data)\n",
    "            if len(listings_data) >= num_listings:\n",
    "                break\n",
    "\n",
    "        page += 1\n",
    "        time.sleep(1)  # To avoid overwhelming the server with requests\n",
    "\n",
    "    df = pd.DataFrame(listings_data)\n",
    "    return df\n",
    "\n",
    "# Scrape data\n",
    "BASE_URL = 'https://www.wg-gesucht.de/wg-zimmer-in-Berlin.8.0.1.0.html'\n",
    "NUM_LISTINGS = 200\n",
    "wg_data_df = scrape_wg_data(BASE_URL, NUM_LISTINGS)\n",
    "wg_data_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "55b529ab-c210-4af8-8288-b254b4af1728",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "di
}