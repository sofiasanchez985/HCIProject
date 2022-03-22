using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class createBars : MonoBehaviour
{

    public GameObject barPrefab;
    int scale = 10000000;

    void Start()
    {
        /***
         * Covid cases per state since Jan.21, 2020
         * update this data from URL below before testing each time after cleaning with python script
         * https://covid.cdc.gov/covid-data-tracker/#cases_casesper100k
        ***/    

        string[] data = {"Alabama 1291567", "Alaska 236965", "Arizona 1992471", "Arkansas 830310", "California 9045132", "Colorado 1330851", "Connecticut 731868", "Delaware 258671", "Florida 5835800", "Georgia 2482518", "Hawaii 232845", "Idaho 441938", "Illinois 3053185", "Indiana 1688770", "Iowa 757551", "Kansas 769218", "Kentucky 1305808", "Louisiana 1167207", "Maine 233696", "Maryland 1008740", "Massachusetts 1685937", "Michigan 2378439", "Minnesota 1424613", "Mississippi 793390", "Missouri 1406560", "Montana 272105", "Nebraska 477198", "Nevada 711249", "New Hampshire 300941", "New Jersey 2188228", "New Mexico 516171", "North Carolina 2616864", "North Dakota 239442", "Ohio 2666030", "Oklahoma 1029977", "Oregon 701198", "Pennsylvania 2774815", "Rhode Island 341271", "South Carolina 1465739", "South Dakota 236845", "Tennessee 2017766", "Texas 6620575", "Utah 926442", "Vermont 106370", "Virginia 1660606", "Washington 1445223", "West Virginia 496409", "Wisconsin 1580313", "Wyoming 155907", "New York 4947740"};

        foreach (string entry in data)
        {
            string[] state_data = entry.Split(' ');
            string name = state_data[0];
            string cases = state_data[1];
            float height = float.Parse(cases)/scale;
            Debug.Log(name);
            Debug.Log(height);

            GameObject bar = Instantiate(barPrefab, new Vector3(0, 0, 0), Quaternion.identity);
            bar.name = name;

            Vector3 newScale = new Vector3(bar.transform.localScale.x, height, bar.transform.localScale.z);
            bar.transform.localScale = newScale;

            /*
            Vector3 newPos = new Vector3(bar.transform.position.x, 0.776f, bar.transform.position.z);
            bar.transform.position = newPos;
            */

        }
    }

}
