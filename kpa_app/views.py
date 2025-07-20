from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import WheelSpecification, WheelSpecificationSubmission
from .serializers import WheelSpecificationSerializer, WheelSpecificationSubmissionSerializer

@api_view(['GET', 'POST'])
def wheel_specification_view(request):
    if request.method == 'POST':
        # Extract submission data
        submission_data = {
            'form_number': request.data.get('formNumber'),
            'submitted_by': request.data.get('submittedBy'),
            'submitted_date': request.data.get('submittedDate'),
            'created_at': timezone.now()
        }

        fields_data = request.data.get('fields', {})

        # Validate and save submission
        submission_serializer = WheelSpecificationSubmissionSerializer(data=submission_data)
        if submission_serializer.is_valid():
            submission = submission_serializer.save()

            # Manually map camelCase keys to snake_case for model compatibility
            spec_data = {
                "tread_diameter_new": fields_data.get("treadDiameterNew"),
                "last_shop_issue_size": fields_data.get("lastShopIssueSize"),
                "condemning_dia": fields_data.get("condemningDia"),
                "wheel_gauge": fields_data.get("wheelGauge"),
                "variation_same_axle": fields_data.get("variationSameAxle"),
                "variation_same_bogie": fields_data.get("variationSameBogie"),
                "variation_same_coach": fields_data.get("variationSameCoach"),
                "wheel_profile": fields_data.get("wheelProfile"),
                "intermediate_wwp": fields_data.get("intermediateWWP"),
                "bearing_seat_diameter": fields_data.get("bearingSeatDiameter"),
                "roller_bearing_outer_dia": fields_data.get("rollerBearingOuterDia"),
                "roller_bearing_bore_dia": fields_data.get("rollerBearingBoreDia"),
                "roller_bearing_width": fields_data.get("rollerBearingWidth"),
                "axle_box_housing_bore_dia": fields_data.get("axleBoxHousingBoreDia"),
                "wheel_disc_width": fields_data.get("wheelDiscWidth"),
                "submission": submission.id,
                'created_at': timezone.now()
            }

            # Validate and save specification
            spec_serializer = WheelSpecificationSerializer(data=spec_data)
            if spec_serializer.is_valid():
                spec = spec_serializer.save()
                return Response({
                    "message": "Wheel specification submitted successfully.",
                    "submission": submission_serializer.data,
                    "specification": spec_serializer.data
                }, status=status.HTTP_201_CREATED)
            else:
                submission.delete()  # cleanup if spec save fails
                return Response(spec_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(submission_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'GET':
        # Get filters from query params
        form_number = request.GET.get('formNumber')
        submitted_by = request.GET.get('submittedBy')
        submitted_date = request.GET.get('submittedDate')

        filters = {}
        if form_number:
            filters['form_number'] = form_number
        if submitted_by:
            filters['submitted_by'] = submitted_by
        if submitted_date:
            filters['submitted_date'] = submitted_date

        submissions = WheelSpecificationSubmission.objects.filter(**filters)
        response_data = []

        for submission in submissions:
            spec = WheelSpecification.objects.filter(submission=submission).first()
            response_data.append({
                "formNumber": submission.form_number,
                "submittedBy": submission.submitted_by,
                "submittedDate": submission.submitted_date,
                "fields": {
                    "treadDiameterNew": spec.tread_diameter_new if spec else None,
                    "lastShopIssueSize": spec.last_shop_issue_size if spec else None,
                    "condemningDia": spec.condemning_dia if spec else None,
                    "wheelGauge": spec.wheel_gauge if spec else None,
                    "variationSameAxle": spec.variation_same_axle if spec else None,
                    "variationSameBogie": spec.variation_same_bogie if spec else None,
                    "variationSameCoach": spec.variation_same_coach if spec else None,
                    "wheelProfile": spec.wheel_profile if spec else None,
                    "intermediateWWP": spec.intermediate_wwp if spec else None,
                    "bearingSeatDiameter": spec.bearing_seat_diameter if spec else None,
                    "rollerBearingOuterDia": spec.roller_bearing_outer_dia if spec else None,
                    "rollerBearingBoreDia": spec.roller_bearing_bore_dia if spec else None,
                    "rollerBearingWidth": spec.roller_bearing_width if spec else None,
                    "axleBoxHousingBoreDia": spec.axle_box_housing_bore_dia if spec else None,
                    "wheelDiscWidth": spec.wheel_disc_width if spec else None,
                }
            })

        return Response({
            "message": "Filtered wheel specification forms fetched successfully.",
            "success": True,
            "data": response_data
        }, status=status.HTTP_200_OK)
